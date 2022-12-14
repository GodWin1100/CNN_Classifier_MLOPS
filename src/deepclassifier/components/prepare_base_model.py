import tensorflow as tf
from pathlib import Path
from deepclassifier.entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig) -> None:
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top,  # to have ANN after CNN or no
        )
        # https://stackoverflow.com/a/46040835
        # https://machinelearningmastery.com/how-to-use-transfer-learning-when-developing-convolutional-neural-network-models/
        # input_shape, pooling only defined when include_top=False
        self.save_model(self.config.base_model_path, self.model)

    @staticmethod
    def _prepare_full_model(
        model: tf.keras.Model,
        classes: int,
        freeze_all: bool,
        freeze_till: int,
        learning_rate: float,
    ):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units=classes, activation="softmax")(flatten_in)
        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)
        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"],
        )
        full_model.summary()
        return full_model

    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate,
        )
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

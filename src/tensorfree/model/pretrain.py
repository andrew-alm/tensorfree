import numpy as np
from tensorflow.keras.models import Model
import tensorflow.keras.applications as kapps
from tensorfree.model.pretrain_factory import PreTrainFactory
from tensorfree.utils.wrappers import pred_logger
from tensorfree.io.data_factory import photo_grabber, photo_saver


class PredictiveModel:
    """Base Tensorfree Model Object"""

    def __init__(self):
        self.photo_store = None
        self.photo_save = None
        self.pretrained = None

    @pred_logger
    def predict(self, image):
        """A call to the object with an image will generate predications
        based on the specific model type created.

        Parameters
        ----------
        image : np.array
            An (w x h x 3) array representing an image

        Returns
        -------
        predictions : np.array
            Flat probability array representing softmax output for each class
        """
        if len(image.shape) == 3:
            image = np.expand_dims(image, axis=0)

        predictions = self.pretrained(image)
        return predictions

    def get_photos(self, location, **kwargs):
        """Depending on defined location, this will grab the required data
        method to access the photos and save it to instance photo_store.

        Parameters
        ----------
        location : str
            One of 'local', 'gcs', 'aws'
        """
        self.photo_store = photo_grabber(location, **kwargs)

    def save_photos(self, location, **kwargs):
        """This maps the correct photo save location to instance photo_save.

        Parameters
        ----------
        location : str
            One of 'local', 'gcs', 'aws'
        """
        self.photo_save = photo_saver(location, **kwargs)


class NASNetBuilder(PredictiveModel):
    """Builder class to set pretrained model to NASNetLarge"""

    def __init__(self):
        super().__init__()
        self.pretrained = kapps.nasnet.NASNetLarge(weights="imagenet")


class DenseNetBuilder(PredictiveModel):
    """Builder class to set pretrained model to DenseNet201"""

    def __init__(self):
        super().__init__()
        self.pretrained = kapps.densenet.DenseNet201(weights="imagenet")


class MobileNetBuilder(PredictiveModel):
    """Builder class to set pretrained model to MobileNetV2"""

    def __init__(self):
        super().__init__()
        self.pretrained = kapps.mobilenet_v2.MobileNetV2(weights="imagenet")


class InceptionBuilder(PredictiveModel):
    """Builder class to set pretrained model to InceptionResNetV2"""

    def __init__(self):
        super().__init__()
        self.pretrained = kapps.inception_resnet_v2.InceptionResNetV2(
            weights="imagenet"
        )


class VGGBuilder(PredictiveModel):
    """Builder class to set pretrained model to VGG19"""

    def __init__(self):
        super().__init__()
        self.pretrained = kapps.vgg19.VGG19(weights="imagenet")


# Register Model w/ Factory
# Usage model = pretrain.factory.create('Model_name')
factory = PreTrainFactory()
factory.register_pretrain_builders("NASNetLarge", NASNetBuilder())
factory.register_pretrain_builders("DenseNet", DenseNetBuilder())
factory.register_pretrain_builders("MobileNetV2", MobileNetBuilder())
factory.register_pretrain_builders("InceptionResNetV2", InceptionBuilder())
factory.register_pretrain_builders("VGG19", VGGBuilder())

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `model` package."""
from unittest import TestCase
import numpy as np

from tensorfree.model import pretrain


class ModelBuildingTests(TestCase):
    """Test cases for both pretrain.py and pretrain_factory.py"""
    def setUp(self) -> None:
        """Create a mobilenet prediction model to test against"""
        self.model = pretrain.factory.create("MobileNetV2")

    def test_register(self):
        """Verify that the factory register created correct model type"""
        self.assertIsInstance(self.model, pretrain.MobileNetBuilder)

    def test_unknown_model(self):
        """Check that an error is raised if user calls an unknown model name"""
        with self.assertRaises(ValueError):
            model = pretrain.factory.create("UnavailableModel")

    def test_photo_get(self):
        """Confirm that calling get_photos sets instance photo_store"""
        self.assertEqual(self.model.photo_store, None)
        print(self.model.get_photos("local"))
        self.assertTrue(self.model.photo_store)

    def test_photo_save(self):
        """Same test but for photo_save"""
        self.assertEqual(self.model.photo_save, None)
        print(self.model.save_photos("local"))
        self.assertTrue(self.model.photo_save)

    def test_predictions(self):
        """Verify that model was created and is given predictions on images"""
        fake_image_array = np.ones((256, 256, 3))
        fake_predictions = np.ones((1000,))
        predictions = self.model.predict(fake_image_array)
        self.assertTrue(predictions.shape, fake_predictions.shape)

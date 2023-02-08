# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline, ImageException
from Ralph_Lauren.settings import IMAGES_STORE

class ClothingImagePipeline(ImagesPipeline):
  def get_media_requests(self, item, info):
    for image_url in item['image_urls']:
      yield scrapy.Request(image_url)

  def item_completed(self, results, item, info):
    # iterate over the local file paths of all downloaded images
    for result in [x for ok, x in results if ok]:
      path = result['path']
      target_path = os.path.join(IMAGES_STORE, item['image_type'])
      os.rename(os.path.join(IMAGES_STORE, path), target_path)
      if self.IMAGES_RESULT_FIELD in item.fields:
        result['path'] = target_path
        item[self.IMAGES_RESULT_FIELD].append(result)
    return item

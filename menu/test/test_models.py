from django.test import TestCase
from menu.models import Menu, Dish, Date


class ModelsTestCase(TestCase):

    def test_dish_str(self):
        dish = Dish.objects.create(dish_name='Fish & chips',
                                   recipe='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                                          ' Donec gravida sollicitudin odio, et ultrices eros accumsan in.'
                                          ' Duis in est magna. Sed sagittis in libero non lacinia.'
                                          ' Ut quis justo ultrices, fringilla mi sed, feugiat elit. '
                                          ' Curabitur sit amet auctor nunc, non tincidunt quam.'
                                          ' Nam scelerisque nibh quis nisi imperdiet faucibus.'
                                          ' Integer feugiat ipsum ac condimentum ultrices.'
                                          ' Suspendisse aliquam laoreet sem gravida molestie.',

                                   ingredients='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                                          ' Donec gravida sollicitudin odio, et ultrices eros accumsan in.'
                                          ' Duis in est magna. Sed sagittis in libero non lacinia.'
                                          ' Ut quis justo ultrices, fringilla mi sed, feugiat elit. '
                                          ' Curabitur sit amet auctor nunc, non tincidunt quam.'
                                          ' Nam scelerisque nibh quis nisi imperdiet faucibus.'
                                          ' Integer feugiat ipsum ac condimentum ultrices.'
                                          ' Suspendisse aliquam laoreet sem gravida molestie.',
                                   serving="4 serving"
                                   )
        self.assertEqual(str(dish), "Fish & chips")

    def test_date_str(self):
        date = Date.objects.create(day="Sunday", time_days="am")
        self.assertEqual(str(date), "Sunday")
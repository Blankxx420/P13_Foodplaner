from django.test import TestCase
from menu.models import Menu, Dish, Date
from users.models import User


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

    def test_menu_str(self):
        user = User.objects.create()
        dish_1 = Dish.objects.create(dish_name='Fish & chips',
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
                                     serving="4 serving")
        dish_2 = Dish.objects.create(dish_name='Tartiflette',
                                     recipe='Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                                            ' Donec gravida sollicitudin odio, et ultrices eros accumsan in.'
                                            ' Duis in est magna. Sed sagittis in libero non lacinia.'
                                            ' Ut quis justo ultrices, fringilla mi sed, feugiat elit. '
                                            ' Curabitur sit amet auctor nunc, non tincidunt quam.'
                                            ' Nam scelerisque nibh quiset faucibus.'
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
                                     serving="4 serving")
        date_1 = Date.objects.create(day="Sunday", time_days="am")
        date_2 = Date.objects.create(day="Monday", time_days="am")
        menu = Menu.objects.create(menu_name="menu1",
                                   user_menu=user,
                                   menu_date=(date_1, date_2),
                                   menu_dish=(dish_1, dish_2)
                                   )
        self.assertEqual(str(menu), "menu1")
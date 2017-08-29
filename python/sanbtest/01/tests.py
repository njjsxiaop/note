import unittest
from markdown import Helper


class TestTrans(unittest.TestCase):

    text = '''
    ![aa](1.png) <img src="https://static.baydn.com/static/img/logo_v4.png"></img> ![](https://static.baydn.com/static/img/logo_v1.png)
    Hello World! There is an image: <img src="https://static.baydn.com/static/img/logo_v1.png"></img>
    and There is a link: https://www.google.com/search?q=Hello
    and There is a good link: [https://www.google.com/search?q=Hello](https://www.google.com/search?q=Hello)
    and There is a video: <video src="https://v.qq.com/xyz.mp4"></video>
    '''

    result = '''
    ![aa](1.png) <img src="https://static.baydn.com/static/img/logo_v4.png"></img> ![](https://static.baydn.com/static/img/logo_v1.png)
    Hello World! There is an image: <img src="https://static.baydn.com/static/img/logo_v1.png"></img>
    and There is a link: [https://www.google.com/search?q=Hello](https://www.google.com/search?q=Hello)
    and There is a good link: [https://www.google.com/search?q=Hello](https://www.google.com/search?q=Hello)
    and There is a video: <video src="https://v.qq.com/xyz.mp4"></video>
    '''

    img = '1.png'
    img1 = 'https://static.baydn.com/static/img/logo_v4.png'
    img2 = 'https://static.baydn.com/static/img/logo_v1.png'


    def test_deal_complex(self):
        h = Helper(self.text)
        wrapped = h.wrap_links()
        self.assertEqual(wrapped, self.result)
        urls = h.extract_images()
        self.assertIn(self.img, urls)
        self.assertIn(self.img1, urls)
        self.assertIn(self.img2, urls)


if __name__ == '__main__':
    unittest.main()

import os
from app.main import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


def test():
    """运行单元测试"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    print(app.url_map)
    print(app.static_url_path)
    app.run()
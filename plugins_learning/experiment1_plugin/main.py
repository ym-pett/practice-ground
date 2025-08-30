# based on this tutorial https://alysivji.github.io/simple-plugin-system.html
# TODO for next step, put these in separate modules & use importlib to import them!

# this is where we call both our main module, 'internal', and our plugins 
# from 'external'

from internal import MyApplication
from external import HelloWorldPrinter, BonjourMondePrinter


if __name__ == "__main__":

    # Run witout any plugins
    # app = MyApplication()
    # app.run()

    # # Run with one plugin
    # app = MyApplication(plugins=[HelloWorldPrinter()])
    # app.run()

    # # Run with another plugin
    # app = MyApplication(plugins=[BonjourMondePrinter()])
    # app.run()

    # Run with both plugins
    app = MyApplication(plugins=[HelloWorldPrinter(), BonjourMondePrinter()])
    app.run()
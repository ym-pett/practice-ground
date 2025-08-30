# this is the plugin itself. Or rather 2 plugins. Would be in plugins/ on the same level as narwhals

class HelloWorldPrinter:
    def process(self):
        print("First plugin says 'Hello World!'")


class BonjourMondePrinter:
    def process(self):
        print("Second plugin says 'bonjour monde!'")
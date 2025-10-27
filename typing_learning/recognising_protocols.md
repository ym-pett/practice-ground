Based on exchange with type-hero Dan: https://github.com/dangotbanned. He put it so clearly, any changes 
to his original text would have been to the detriment of clarity.

# How to distinguish Protocols from regular classes in code: 

You can tell if something is a `Protocol` if the class definition lists `Protocol` in it's bases


```python
class IAmAProto(Protocol): ...
```

This _doesn't_ extend to subclasses:

```python
class NotAProto(IAmAProto): ...  # regular class, implementing `IAmAProto`
```

But you _can_ define a subprotocol, by adding `Protocol` to the bases:

```python
class SubProto(IAmAProto, Protocol): ...
```
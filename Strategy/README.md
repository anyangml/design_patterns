# Strategy Pattern

![Strategy_UML](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/anyangml/design_patterns/main/Strategy/uml.txt)


## Thought 
- Instead of using the `Polymorphism` concept by defining abstractmethod in the `Character` class, an interface strategy class is used. This allows more flexiblility, the concret instant of `Character` like `king` is not restricted to a single type of weapon.
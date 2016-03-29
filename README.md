# Hexagonal Python

An experiment in writing a python application with a Hexagonal design.

See <http://alistair.cockburn.us/Hexagonal+architecture>.

The basic idea is that you have a core application that is decoupled from the outside world.
Communication with the outside world happens through ports (think "interfaces") where you can plug in adapters (think "concrete implementations of interfaces").

For example, this application is a wiki.
There will be a `core` that contains the business logic for creating, listing, updating, and versioning pages.
There will be two ports for delivering this application to the real world: `ui` and `db`
For each port, there will be two adapters: in production they will be implemented by Django (with a `ui` adapter implemented by the view layer, and a `db` adapter implemented by the model layer), and in tests they will be implemented by test doubles.

The API (boundary) of the core will be use case objects.

All dependencies should point inwards, and never cross multiple boundaries.
For example:

* Django views _may_ depend on (import) the use cases.
* The use cases _may_ depend on (import) core functions/objects/entities.
* Django views _may not_ depend on (import) core functions/objects/entities.
* The use cases _may not_ depend on (import) Django views/models.

Data going into and out of a use case will be built-in python data structures (strings, lists, dicts).

Future plans to test if this design scales as requirements expand and change:

* a notification port (redis pub/sub?)
* an alternative ui (wxPython? django rest framework? background jobs?)

## Running the tests

Run:

```
nosetests
```

or run them automatically when files change (using [testtube](https://github.com/thomasw/testtube)) with:

```
stir
```

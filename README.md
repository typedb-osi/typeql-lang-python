[![Discord](https://img.shields.io/discord/665254494820368395?color=7389D8&label=chat&logo=discord&logoColor=ffffff)](https://vaticle.com/discord)
[![Discussion Forum](https://img.shields.io/discourse/https/forum.vaticle.com/topics.svg)](https://forum.vaticle.com)
[![Stack Overflow](https://img.shields.io/badge/stackoverflow-typedb-796de3.svg)](https://stackoverflow.com/questions/tagged/typedb)
[![Stack Overflow](https://img.shields.io/badge/stackoverflow-typeql-3dce8c.svg)](https://stackoverflow.com/questions/tagged/typeql)

# TypeQL Language Library for Python

TypeQL language library for Python will allow you to construct TypeQL queries programmatically, as opposed to manual string concatenations. For example, take the following native TypeQL query.

```typeql
match $x isa person, has name "alice", has age 32;
``` 

The native TypeQL query above can be constructed programmatically in Python using this library, in the following way.

```java
TypeQL.match(var("x").isa("person").has("name", "alice").has("age", 32));
```

This library is still under development by the community. You are welcome to contribute to this project development. You can learn more about TypeDB and TypeQL through [vaticle/typedb](https://github.com/vaticle/typedb) and [vaticle/typeql](https://github.com/vaticle/typeql).


# Notes : 
#### **/!\Project still under developpement**

# Kedro History

The intent of this repo is to seve as a playground for `kedro-diff`.

``` bash
$ kedro diff b49071b

╭──────────────────────────────────────────────────────── kedro-diff ─╮
│ modified: __default__                                               │
╰─────────────────────────────────────────────────────────────────────╯
+ <lambda>(None) ->
    name:       <lambda>(None) ->
    inputs:     []
    outputs:    ['range']
    tags:       []
+ <lambda>(None) ->
    name:       <lambda>(None) ->
    inputs:     []
    outputs:    ['range_two']
    tags:       []
+ <lambda>() ->
    name:       <lambda>() ->
    inputs:     ['range']
    outputs:    ['range_squared']
    tags:       []
+ <lambda>() ->
    name:       <lambda>() ->
    inputs:     ['range_two']
    outputs:    ['range_two_squared']
    tags:       []
╭──────────────────────────────────────────────────────── kedro-diff ─╮
│ modified: history_nodes                                             │
╰─────────────────────────────────────────────────────────────────────╯
+ <lambda>(None) ->
    name:       <lambda>(None) ->
    inputs:     []
    outputs:    ['range']
    tags:       []
+ <lambda>(None) ->
    name:       <lambda>(None) ->
    inputs:     []
    outputs:    ['range_two']
    tags:       []
+ <lambda>() ->
    name:       <lambda>() ->
    inputs:     ['range']
    outputs:    ['range_squared']
    tags:       []
+ <lambda>() ->
    name:       <lambda>() ->
    inputs:     ['range_two']
    outputs:    ['range_two_squared']

```


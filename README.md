# Kedro History

The intent of this repo is to seve as a playground for `kedro-diff`.

``` bash
$ kedro diff b49071b  2385c4

╭──────────────────────────────────────────────────────── kedro-diff ─╮
│ modified: __default__                                               │
╰─────────────────────────────────────────────────────────────────────╯
+ <lambda>(None) ->
    name:       <lambda>(None) ->
    inputs:     []
    outputs:    ['range']
    tags:       []
╭──────────────────────────────────────────────────────── kedro-diff ─╮
│ modified: history_nodes                                             │
╰─────────────────────────────────────────────────────────────────────╯
+ <lambda>(None) ->
    name:       <lambda>(None) ->
    inputs:     []
    outputs:    ['range']
    tags:       []

```

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


## diff by branch name

Here are our list of branches

```bash
$ git branch
  init
* main
  range
  range_squared
```

We can run `kedro diff` accross any two branches.  They can be compared to
other branches, commits, or `HEAD` by default.

``` bash
# all 6 of these will return the same result
$ kedro diff range_squared main
$ kedro diff range_squared 417b82967
$ kedro diff range_squared...417b82967
$ kedro diff b49071b  2385c4
$ kedro diff b49071b...2385c4
$ kedro diff range_squared
╭──────────────────────────────────────────────────────── kedro-diff ─╮
│ modified: __default__                                               │
╰─────────────────────────────────────────────────────────────────────╯
+ <lambda>(None) ->
    name:       <lambda>(None) ->
    inputs:     []
    outputs:    ['range_two']
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
    outputs:    ['range_two']
    tags:       []
+ <lambda>() ->
    name:       <lambda>() ->
    inputs:     ['range_two']
    outputs:    ['range_two_squared']
    tags:       []

```

## deleted nodes


``` bash
$  kedro diff main..delete_squared
╭─────────────────────────────────────────────────────────────────────────────────────── kedro-diff ─╮
│ modified: __default__                                                                              │
╰────────────────────────────────────────────────────────────────────────────────────────────────────╯
- <lambda>() ->
    name:      <lambda>() ->
    inputs:    ['range']
    outputs:   ['range_squared']
    tags:      []
- <lambda>() ->
    name:      <lambda>() ->
    inputs:    ['range_two']
    outputs:   ['range_two_squared']
    tags:      []
╭─────────────────────────────────────────────────────────────────────────────────────── kedro-diff ─╮
│ modified: history_nodes                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────╯
- <lambda>() ->
    name:      <lambda>() ->
    inputs:    ['range']
    outputs:   ['range_squared']
    tags:      []
- <lambda>() ->
    name:      <lambda>() ->
    inputs:    ['range_two']
    outputs:   ['range_two_squared']
    tags:      []
```

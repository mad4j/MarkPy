# MarkPy Samples

## Heading samples

Python code  

```python
d.add_h1("Heading level 1")
d.add_h2("Heading level 2")
d.add_h3("Heading level 3")
d.add_h4("Heading level 4")
d.add_h5("Heading level 5")
d.add_h6("Heading level 6")
```

Generated Markdown code  

```markdown
# Heading level 1

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6
```

Rendered Markdown code  

# Heading level 1

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6

--------------------------------------------------------------------------------

## Emphasys samples

Python code  

```python
d.add_para(em.bold("bold"))
d.add_para(em.italic("italic"))
d.add_para(em.code("code"))
d.add_para(em.highlight("highlight"))
```

Generated Markdown code  

```markdown
`` **bold**  

*italic*  

`code`  

==highlight== ``
```

Rendered Markdown code  

**bold**  

*italic*  

`code`  

==highlight==  

--------------------------------------------------------------------------------

## Sections samples

Python code  

```python
d.add_para(text)
d.add_quote(text)
d.add_code(text)
```

Generated Markdown code  

```markdown
`` This is an sample section text.  

> This is an sample section text.

```text
This is an sample section text.
``` ``
```

Rendered Markdown code  

This is an sample section text.  

> This is an sample section text.

```text
This is an sample section text.
```

--------------------------------------------------------------------------------

## Lists samples

### Unordered lists samples

Python code  

```python
d.add_ul('One. This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
d.add_ul('Two. This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
d.add_ul('Three. This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
```

Generated Markdown code  

```markdown
* One. This is a very long line and should be splitted.  This is a very long
  line and should be splitted. This is a very long line and should be splitted.

* Two. This is a very long line and should be splitted.  This is a very long
  line and should be splitted. This is a very long line and should be splitted.

* Three. This is a very long line and should be splitted.  This is a very long
  line and should be splitted. This is a very long line and should be splitted.
```

Rendered Markdown code  

* One. This is a very long line and should be splitted.  This is a very long
  line and should be splitted. This is a very long line and should be splitted.

* Two. This is a very long line and should be splitted.  This is a very long
  line and should be splitted. This is a very long line and should be splitted.

* Three. This is a very long line and should be splitted.  This is a very long
  line and should be splitted. This is a very long line and should be splitted.

### Definition lists samples

Python code  

```python
d.add_dl('One.', 'This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
d.add_dl('Two.', 'This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
d.add_dl('Three.', 'This is a very long line and should be splitted.  This is a very long line and should be splitted. This is a very long line and should be splitted.')
```

Generated Markdown code  

```markdown
One.
: This is a very long line and should be splitted.  This is a very long line and
should be splitted. This is a very long line and should be splitted.

Two.
: This is a very long line and should be splitted.  This is a very long line and
should be splitted. This is a very long line and should be splitted.

Three.
: This is a very long line and should be splitted.  This is a very long line and
should be splitted. This is a very long line and should be splitted.
```

Rendered Markdown code  

One.
: This is a very long line and should be splitted.  This is a very long line and
should be splitted. This is a very long line and should be splitted.

Two.
: This is a very long line and should be splitted.  This is a very long line and
should be splitted. This is a very long line and should be splitted.

Three.
: This is a very long line and should be splitted.  This is a very long line and
should be splitted. This is a very long line and should be splitted.

--------------------------------------------------------------------------------


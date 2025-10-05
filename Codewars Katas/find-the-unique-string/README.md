# [Find the unique string](https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3)

- **Completed at:** 2025-10-05

- **Completed languages:** python

- **Tags:** Fundamentals, Algorithms, Arrays, Strings

- **Rank:** 5 kyu

## Description

There is an array of strings. All strings contains similar _letters_ except one. Try to find it!

```javascript
findUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) === 'BbBb'
findUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) === 'foo'
```

```php
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]); // => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]); // => 'foo'
```

```python
find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
```

```cobol
      FindUniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])
      * => result = 'BbBb'
      FindUniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])
      * => result = 'foo'
```

Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.

This is the second kata in series:

1. [Find the unique number](https://www.codewars.com/kata/585d7d5adb20cf33cb000235)
2. Find the unique string (this kata)
3. [Find The Unique](https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5)
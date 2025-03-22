This is your new *vault*.

Make a note of something, [[create a link]], or try [the Importer](https://help.obsidian.md/Plugins/Importer)!

When you're ready, delete this **note** and make the vault your own.

# hello there

## hello

### hello where

#### where is it?

```java
public int count8(int n) {
    // Call the helper method with the initial previous digit as -1 (invalid)
    return count8Helper(n, -1);
}

private int count8Helper(int n, int prevDigit) {
    // Base case: no digits left
    if (n == 0) {
        return 0;
    }
    // Extract the rightmost digit
    int currentDigit = n % 10;
    // Check if the current digit is 8
    if (currentDigit == 8) {
        // Check if the previous digit was also 8
        if (prevDigit == 8) {
            return 2 + count8Helper(n / 10, currentDigit);
        } else {
            return 1 + count8Helper(n / 10, currentDigit);
        }
    } else {
        return count8Helper(n / 10, currentDigit);
    }
}
```
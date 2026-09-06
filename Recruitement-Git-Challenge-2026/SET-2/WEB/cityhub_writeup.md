#cityhub_webexp
## Challenge

The flag was divided into seven parts and hidden in different places on the website. I checked `robots.txt`, the page source, CSS, network requests, files and browser cookies.

## Checking robots.txt

I opened `robots.txt` and found:

```text
User-agent: \\\*
Disallow: /itshallbedone.html
```

The `Disallow` entry showed a hidden page:

```text
/itshallbedone.html
```

While following the page, I obtained the first fragment:

```text
Part 1 = bios{W31c0m
```

## Checking the Hidden Pages

After opening the hidden page, I reached:

```text
/lanif.html
```

Its source included these files:

```text
/files/style.css
/files/john.gif
```

The page also displayed a clue about a cookie, so I knew that I had to check the browser cookies later.

## Checking the CSS

I opened `/files/style.css` and found a comment containing:

```css
/\\\* part 2 --> 3\\\_t0\\\_ \\\*/
```

This gave the second fragment:

```text
Part 2 = 3\\\_t0\\\_
```

The other page content gave:

```text
Part 3 = th3\\\_p4r
```

## Checking john.gif

I downloaded `/files/john.gif` and checked its bytes. It started with:

```text
47 49 46 38 39 61
```

This is the normal `GIF89a` header. I inspected the GIF and obtained:

```text
Part 4 = ts\\\_0f\\\_
```

## Checking Network Requests

I opened Developer Tools using `F12` and selected the **Network** tab. I checked the requests for `lanif.html`, `style.css` and `john.gif`.

From this step, I obtained:

```text
Part 5 = th3\\\_w3b
```

The request for `/lanif.html` also showed that the previous page was `/itshallbedone.html`.

## Checking Cookies

I opened:

```text
Developer Tools → Application → Cookies
```

The cookie value was:

```text
part7=y4yy}
```

Therefore:

```text
Part 7 = y4yy}
```

## Recovered Parts

```text
Part 1 = bios{W31c0m
Part 2 = 3\\\_t0\\\_
Part 3 = th3\\\_p4r
Part 4 = ts\\\_0f\\\_
Part 5 = th3\\\_w3b
Part 6 = NOT FOUND
Part 7 = y4yy}
```

The incomplete flag was:

```text
bios{W31c0m3\\\_t0\\\_th3\\\_p4rts\\\_0f\\\_th3\\\_w3b\\\[PART6]y4yy}
```

## Conclusion

I found six of the seven flag parts by checking different parts of the website. Part 6 was still missing, so `\\\[PART6]` must be replaced after that fragment is found.


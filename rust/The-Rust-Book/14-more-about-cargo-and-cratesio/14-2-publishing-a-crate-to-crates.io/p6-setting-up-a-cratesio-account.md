# Setting Up a Crates.io Account


Before you can publish any crates, you need to create an account on crates.io and get an API token.
To do so, visit the home page at crates.io and log in via a GitHub account. (The GitHub account is
currently a requirement, but the site might support other ways of creating an account in the future.)
Once you're logged in, visit your account settings at https://crates.io/me/ and retrieve your API key.
Then run cargo login command with your API key, like this:

$ cargo login abcdefghijklmnopqrstuvwxyz012345

This command will inform Cargo of your API token and store it locally in ~/.cargo/credentials. Note
that this token is a *secret*: do not share it with anyone else. If you do share it with anyone for any
reason, you should revoke it and generate a new token on crates.io

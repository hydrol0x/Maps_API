# Install packages

To install dependencies

`pip install -r requirements.txt`

# Usage

Default return [Formatted address, Formatted phone number, Place name]

When run from main file, will prompt for a query. Query is any text such as "Hospital" or "123 Garden Rd."

Through `getID()` function can also decide to search with phone-number.

Through `getPlace()` can specify additional fields to return.

`search()` is default function called to search query, second parameter can also specify json output.

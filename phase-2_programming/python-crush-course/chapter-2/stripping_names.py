#!/usr/bin/env python3

name_with_whitespace = "\tDenzel Washington\n"
print(f"Original name with whitespace: '{name_with_whitespace}'")

# Using stripping functions
print(f"Using lstrip(): '{name_with_whitespace.lstrip()}'")
print(f"Using rstrip(): '{name_with_whitespace.rstrip()}'")
print(f"Using strip(): '{name_with_whitespace.strip()}'")
# TODO: provide a descriptive docstring for the module as done in prev labs

# TODO: import required packages and modules referring to previous labs
# and Guttag Chapter 7 about modules

# TODO: create a Typer object to support the command-line interface

# TODO: define a PalindromeCheckingApproach enumeration with these options:
# --> "RECURSIVE"
# --> "REVERSE"
# NOTE: refer to previous labs for reference


# TODO: add the typer cli function decorator as shown in previous labs

# TODO: implement a command-line interface using typer that produces
# output as shown below. You can find information about the CLI name,
# the options, the expected values of the options, and the display
# text below.

# EXAMPLE ONE
# poetry run palindromechecker --word civic --approach recursive

# ✨ Awesome, using the recursive approach for palindrome checking!

# 🔖 Going to check to see if the word "civic" is a palindrome!

# 😆 Is this word a palindrome? Yes, it is!

# EXAMPLE TWO
# poetry run palindromechecker --word civic --approach reverse

# ✨ Awesome, using the reverse approach for palindrome checking!

# 🔖 Going to check to see if the word "civic" is a palindrome!

# 😆 Is this word a palindrome? Yes, it is!

# EXAMPLE THREE - notice any default values
# poetry run palindromechecker --help

# Usage: palindromechecker [OPTIONS]
#
#   Use a method to determine if an input string is a palindrome or not.
#
# Options:
#   --word TEXT                     [required]
#   --approach [recursive|reverse]  [default: reverse]
#   --install-completion            Install completion for the current
#                                   shell.
#
#   --show-completion               Show completion for the current shell,
#                                   to copy it or customize the
#                                   installation.
#
#   --help                          Show this message and exit.

# NOTE: When you are setting the default values of the --approach variable
# you may need to extract a value from PalindromeCheckingApproach by
# using the .value class attribute. Some examples can be found here:
# https://github.com/tiangolo/typer/issues/290

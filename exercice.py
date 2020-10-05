#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_brackets(text, brackets):
	# ouvrants
	brackets[0::2]
	# fermants
	brackets[1::2]
	opening_brackets = dict(zip(brackets[0::2], brackets[1::2])) #ouvrant a fermant
	closing_brackets = dict(zip(brackets[1::2], brackets[0::2])) #fermant a ouvrant

	brackets_stack = []

	for chr in text:
		if chr in opening_brackets:
			brackets_stack.append(chr)
		elif chr in closing_brackets:
			if len(brackets_stack) == 0 or brackets_stack[-1] != closing_brackets[chr]:
				return False
			brackets_stack.pop()

	return len(brackets_stack) == 0

def remove_comments(full_text, comment_start, comment_end):
	text = full_text
	while True:
		start = text.find(comment_start)
		end = text.find(comment_end)
		if start == -1 and end == -1:
			return text
		if end < start or (start == -1) != (end == -1):
			return None
		text[:start] + text[end + len(comment_end):]
# 	le end + len cest le debut de la balise + sa longueur soit **/


def get_tag_prefix(text, opening_tags, closing_tags):
	return (None, None)

def check_tags(full_text, tag_names, comment_tags):
	return False


if __name__ == "__main__":
	brackets = ("(", ")", "{", "}")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, /* OOGAH BOOGAH */world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()


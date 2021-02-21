#! /bin/sh

repository=$(basename `git rev-parse --show-toplevel`)

format="{%n \"hash\": \"%H\",%n \"parent\": \"%P\", %n \"author_name\":\"%an\", %n \"author_email\":\"%ae\", %n \"author date\":\"%ad\" , %n \"committer_name\": \"%cn\", %n \"commiter_email\": \"%ce\", %n \"committed_date\": \"%cd\" , %n \"ref name\": \"%S\" ,%n \"message\": \"%f\",%n \"repo_name\": \"$repository\",%n \"parents\": \"%P\"%n}"

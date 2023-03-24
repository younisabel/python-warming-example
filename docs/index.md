# Python Warming Example

This example extracts and shows data from an excel file,
which contains information about the GHG emissions of
food. Additionally, it shows the food consumed per country.

Open issues are documented in the [issues](issues.md) page.

## Getting started

In order to get started with implementing a feature to fix one
of the open [issues](issues.md), first start by creating a new
feature branch with git. You can use your IDE (like PyCharm) or
the command line:

```commandline
git checkout -b feature-issueX-YZ
```

where X is the issue number (or a description) and YZ are your
initials.

### Commit your changes

As soon as you finished to implement the feature, commit your changes.
Again, either use your IDE, or the command line with the following
command:

```commandline
git add LIST OF CHANGED FILES
git commit -m "COMMIT MESSAGE"
git push -u origin feature-issueX-YZ
```

### Merging feature branches

If you are responsible for merging the different feature branches, you first
need to swith to the main branch, pull the (colleagues') changes from the
remote repository and finally merge it:

```commandline
git checkout main
git pull
git merge feature-issueX-YZ
``` 

Finally, push the merged main branch to the remote repository:

```commandline
git push origin main
```

### Tagging

Are you ready with all the features that needed to be implemented into a specific
version of the program? Then, you can tag the current state of the program:

```commandline
git tag vX.Y.Z # where X is the major version, Y the minor version and Z the bug fix version
git push --tags
```

For simplicity, use v0.2.0 in the first round.

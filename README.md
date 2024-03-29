# BIPIC

This PIC code has been developed since 2022 at the Budker Institute of Nuclear Physics as an alternative to 
[ASTRA](https://www.desy.de/~mpyflo/), 
[WARP](https://bitbucket.org/berkeleylab/warp/), 
[XTRACK](https://xsuite.readthedocs.io/en/latest/) 
and other codes. 

For particle dynamics simulation using finite difference scheme relativistic.

## Table of content 

-   [Getting Started](#getting-started)
    -   [Documentation](#documentation)
        -   [Adding a new section](#adding-a-new-section)
    -   [Additional resources](#additional-resources)
-   [Prerequisites](#prerequisites)
    -   [Latex](#latex)
-   [Useful Resources](#useful-resources)
    -   [IDE](#ide)
-   [Authors](#authors)
-   [Licence](#license)
-   [Contributing](#contributing)
    -   [Dependencies](#dependencies)
    -   [Formatting](#formatting)
    -   [Tests](#tests)
    -   [Maintaining](#maintaining)

## Getting Started

### Documentation

The documentation contains all the Latex files needed to generate documentation. 
The main source files are located in the `documentation/src`.

* [main.tex](/docs/src/main.tex) is documentation source file. 
The final PDF can be found [here](/docs/out/main.pdf).

[main.tex](/docs/src/main.tex) is the source file that Latex compiler will use to generate the paper. 
However, in order to keep the code cleaner, the main sections of the paper are all located in the [sections](/docs/src/sections). 
In this way you will experience less merging issues when two or more people are working on the same doc.

Just edit the text in the relative Latex file (e.g., introduction, methodology, etc.) and you should be ready to go. 
No need to change any other file.

#### Adding a new section

Just copy a section file (e.g., [introduction.tex](/docs/src/sections/introduction.tex)) paste it in the same directory. 
Rename the pasted file (e.g. first_chapter.tex) and add this file to [main.tex](/docs/src/main.tex).

### Additional Resources

Alternatively you can find great resources on the 
[Overleaf Tutorial website](https://www.overleaf.com/learn/latex/Tutorials) or on 
[Latex wikibooks](https://en.wikibooks.org/wiki/LaTeX).

## Prerequisites

#### Latex

Latex IDE and compiler installed locally on your machine. 
We recommend using a PyCharm plugin called [TeXiFy IDEA](https://plugins.jetbrains.com/plugin/9473-texify-idea) as IDE and 
[miktex](https://miktex.org) as Latex compiler  

Alternatively you can push your code to Overleaf using git and only use Overleaf. 
We would discourage you from doing this! Overleaf should only be used for the review.

## Useful Resources

### IDE

You may want to take advantage of the power of IDEs. 
For Python We would recommend using [PyCharm](https://www.jetbrains.com/pycharm/). 

Alternatives are:

* [Visual Studio](https://code.visualstudio.com)
* [Atom](https://atom.io/)

### Git

You should install [git](https://git-scm.com) on your computer. And have [GitHub](https://github.com) account.

## Authors

* **[Vyacheslav Fedorov](https://github.com/fuodorov)** - *Initial work*
* **[Danila Nikiforov](https://github.com/Danila-Nikiforov)** - *Initial work*

See also the list of [contributors](https://github.com/binp-dev/redpic/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Contributing

### Dependencies
Use `make deps` command to install library, its production and development dependencies.

### Formatting
Use `make format` to autoformat code with black tool. 

### Tests
Use `make lint` to run only linters for current python version

### Maintaining
If pull request consists of several meaningful commits, that should be preserved, 
then use "Rebase and merge" option. Otherwise use "Squash and merge". 

New release (changelog, tag and pypi upload) will be automatically created 
on each push to master via Github Actions workflow.
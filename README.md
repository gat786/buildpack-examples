# Buildpack samples

This repository was setup to showcase the capabilities of Pack CLI.

There are 3 examples of Cloud Functions being created in 3 different languages
[Nodejs](./nodejs), [Python](./python) & [Java](./java) the code in them is pretty 
simple and is only created to showcase what a function code looks like.

In each of those directories you will find a `project.toml` file which is a 
configuration file created to store configuration in the [TOML](https://toml.io/en/) 
format. The contents of this file define the name of the actual function 
instance that is considered to be a target when building a Docker image for
a Cloud Run Function.

In our Github actions present [here](./.github/workflows/buildpacks.yaml) file we 
1. Install the Pack CLI
2. Run the command `pack build --builder gcr.io/buildpacks/builder .` from the code directories.
3. Pack CLI would build a docker image for us and we can then push the docker image thus created to any container image compliant OCI registry, in our case we upload it to [ghcr](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

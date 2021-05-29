# NetCon-Jenkins-Deployment

This repository contains an API that is used to convert some networking stuff (cidr to mask, mask to cidr and many others). 

It also displays how a simple application could be maintained useing CI/CD on Jenkins and of course Kuberntes for application management and hosting on AWS. 

![jenkins Deploy-1](https://user-images.githubusercontent.com/47984109/119967755-9c22cc00-bfa4-11eb-82e3-247eed3aeaa9.png)


## Application Overview

The API has 3 endpoints as follows:
- First endpoint converts Subnet Mast to CIDR format
- Second endpoint return the CIDR value of a given Subnet Mask
- Third endpoint simply validates an IPv4.

e.g.

```
curl localhost/cidr-to-mask?value=24
{
  "function": "cidrToMask",
  "input": "24",
  "output": "255.255.255.0"
}
```

```
curl localhost/mask-to-cidr?value=255.255.0.0
{
  "function": "maskToCidr",
  "input": "255.255.0.0",
  "output": "16"
}

```

```
curl localhost/ip-validation?value=255.255.0.0
{
  "function": "ipv4Validation",
  "input": "255.255.0.0",
  "output": true
}

```

### Continuous Integration
  * There is a CI pipeline on Jenkins
  * Ideally the pipelines are checked in code (Jenkinsfile or Scripts).
  * Tets are automated that every time a change is pushed to the repository, the CI builds
  * The artifacts (Docker Image) are stored in a registrywith appropriate tagging.
  * Each of the branches are protected.
  
### Continuous Delivery

  * The CD pipeline is already defined and prod/test enviroment deployed.
  * Deployed with no expected downtime in production.

## Infrastructure Management

  You will need to have access to the following from your own end:

  * Jenkins server
  * Kubernetes Cluster


> **Note:** Be aware that the installation of some plugins may cause a missconfiguration of the Jenkins server and your work will be lost.

### Using Docker Builder
  * Docker is already integrated with Jenkins, in a job you could use this
  command to build an image

```
 docker build -t <your-name>:some-tag .
```

  * You will need to push data to a remote docker registry. 

### Deploying to Kubernetes

In this section you will need to know.

  * How to deploy to kubernetes.
  * The kube config file.
  * try to create a secret file in jenkins with your configuration file

> **Note:** Make sure you have the different branches on your host application repository


#### How to deploy to Kubernetes.

> **Note:** Make sure to use kubeconfig with the value set up in the
> Jenkins Credentials Section.

  * Update the version of the image in the kubernetes cluster, e.g.:
    - `kubectl --kubeconfig=${KUBECONFIG} --namespace=<ENVIRONMENT>
    set image deployment/api api=name/api:tag`

> **Note:** This only works from jenkins.

## Hire me
Looking for an engineer to build and automate your next application infrastruture/architecture to work remotely? Get in touch: sbayo971@gmail.com

## How can I thank you?
Why not star the Github repo? I'd love the attention! Why not share the link for this repository on Twitter,Hackernews or Destructoid ? Spread the word!

Don't forget to follow me on [twitter](https://twitter.com/SamuelArogbonlo). Also, you could see other things I do in the software enviroment via my [website](https://samuelarogbonlo.github.io/)

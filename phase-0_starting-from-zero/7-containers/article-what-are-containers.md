# What are Containers

Containers are a way to package an application with the things it needs to run.

That package can include the application code, runtime, libraries, tools, and settings. This helps the application run more consistently across different environments, such as a developer laptop, a test server, or production.

Source: [Docker - What is a container?](https://www.docker.com/resources/what-container/)

## Simple Definition

| Term | Beginner-friendly meaning |
| --- | --- |
| **Container** | A small, isolated environment that runs an application and its dependencies. |
| **Container Image** | A saved package that includes the application and everything it needs to run. |
| **Container Runtime** | The software that starts and runs containers. Docker Engine is one example. |
| **Dependency** | Something an application needs to work, such as a library, tool, or runtime. |

## Why Containers Matter

Before containers, software could behave differently in different environments.

For example, an app might work on a developer's laptop but fail on a server because the server has a different version of Python, Node.js, Java, or a system library.

Containers help solve this by packaging the application and its dependencies together.

| Problem | How containers help |
| --- | --- |
| **"It works on my machine"** | The same container can run on a laptop, test server, or production environment. |
| **Missing dependencies** | The container image includes what the application needs to run. |
| **Different environments** | Containers isolate the application from many differences in the host system. |
| **Slow setup** | Teams can start a container from an image instead of manually installing everything. |

## Container Images and Containers

| Concept | What it means |
| --- | --- |
| **Image** | The blueprint or package for the application. |
| **Container** | A running instance of that image. |

Think of an image like a recipe and a container like the meal made from that recipe.

You can use the same image to start the same application many times.

## What Goes Inside a Container Image

| Item | Why it is included |
| --- | --- |
| **Application code** | The actual program the team wrote. |
| **Runtime** | The language or platform needed to run the app, such as Python, Node.js, or Java. |
| **Libraries** | Extra packages the app depends on. |
| **System tools** | Small tools the app may need while running. |
| **Settings** | Configuration needed for the app to start correctly. |

## Containers vs Virtual Machines

Containers and virtual machines both help isolate applications, but they work differently.

| Containers | Virtual Machines |
| --- | --- |
| Package the application and dependencies. | Package the application, dependencies, and a full operating system. |
| Share the host machine's operating system kernel. | Each VM runs its own operating system. |
| Usually start faster. | Usually take longer to start. |
| Usually use fewer resources. | Usually use more CPU, memory, and storage. |
| Good for running many applications efficiently. | Good when you need strong separation with full operating systems. |

## Beginner Example

Imagine a team builds a web app that needs:

- Node.js
- Several npm packages
- Environment settings
- A command to start the server

Without containers, every developer and server must install the correct versions manually.

With containers, the team creates a container image that includes the app and its dependencies. Then anyone can run the same image and get the same setup.

## Where Containers Are Used

| Environment | How containers help |
| --- | --- |
| **Development** | Developers can run the same app setup locally. |
| **Testing** | Test environments can be recreated quickly. |
| **CI/CD pipelines** | Pipelines can build, test, and package applications in a repeatable way. |
| **Production** | Applications can be deployed consistently across servers or cloud platforms. |

## Key Idea

Containers make applications easier to package, share, and run.

They help teams move software across environments with fewer surprises because the application and its dependencies travel together.

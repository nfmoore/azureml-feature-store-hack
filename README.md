# Azure ML Feature Store Hack

## Overview

The Azure ML Feature Store is a centralized repository for storing, managing, and sharing machine learning features. It allows you to store and manage features independently of the models that use them, making it easier to reuse features across different models. The feature store also provides versioning and lineage tracking, which helps ensure that the features used in your models are consistent and up-to-date.

In this repository, you will find notebooks to support a developer-focused hands-on self-directed hackathon that demonstrates how to use the Azure ML Feature Store to manage and share features.

The hackathon covers a range of topics, including:

- Creating and managing feature sets
- Registering features in the feature store
- Retrieving features from the feature store
- Using features when training a machine learning model
- Performing batch inference

## Prerequisites

To complete this hack the following must be available and configured:

- An Azure ML Feature Store
- An Azure ML Workspace (with access to the Azure ML Feature Store)
- Sample data available in an Azure ML Datastore
- A compute cluster in the Azure ML Workspace (with access to the sample data)
- All users and managed identities with necessary permissions

Before commencing the hackathon add all environment variables in the `environment/variables` file. These will be used by the `python-dotenv` library to configure necessary environment variables.

## Resources

You can use the following resources to help you complete the hackathon:

- [Managed Feature Store Concepts](https://learn.microsoft.com/en-us/azure/machine-learning/concept-what-is-managed-feature-store?view=azureml-api-2)
- [Managed Feature Store Tutorials](https://learn.microsoft.com/en-us/azure/machine-learning/tutorial-get-started-with-feature-store?view=azureml-api-2&tabs=SDK-track)
- [Azure ML Feature Store Sample GitHub Repository](https://github.com/Azure/azureml-examples/tree/main/sdk/python/featurestore_sample)

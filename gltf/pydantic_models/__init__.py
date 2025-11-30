"""
Pydantic v2 models for the glTF 2.0 core schema.

This module defines Pydantic models that map the glTF 2.0 JSON
structure to Python classes for loading and validating.

There are spec-enforcing validators (all end with `_gltf_spec`).
    - GLTFSpecError(ValueError) is raised for MUST-level violations.
    - GLTFSpecWarning(UserWarning) is raised for SHOULD-level violations (and when going against advisories in the glTF spec).

Additional properties are allowed for all Pydantic models (per the spec).

GLTFBase and GLTFNamed are base classes that are implied by the spec (and exist in their JSON Schema anyway).

(DDS textures have been added to the default supported image formats since projects I want to work on use it)

Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html
"""

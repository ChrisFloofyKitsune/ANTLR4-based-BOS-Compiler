from __future__ import annotations

from typing import Optional, Literal, Annotated

from pydantic import Field

from gltf.pydantic_models.annotation import IndexRef
from gltf.pydantic_models.base_definitions import GLTFNamed, GLTFBase


class Animation(GLTFNamed):
    """
    A keyframe animation.

    Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-animation
    """

    channels: list[Animation.Channel] = Field(min_length=1)
    """
    An array of animation channels.
    
    An animation channel combines an animation sampler with a target property being animated.

    Different channels of the same animation MUST NOT have the same targets.
    """

    samplers: list[Animation.Sampler] = Field(min_length=1)
    """
    An array of animation samplers.
    
    An animation sampler combines timestamps with a sequence of output values
    and defines an interpolation algorithm.
    """

    class Channel(GLTFBase):
        """
        An animation channel combines an animation sampler with a target property being animated.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-animation-channel
        """

        sampler: Annotated[int, Field(ge=0), IndexRef('Animation.Sampler')]
        """
        The index of a sampler in this animation used to compute the value
        for the target, e.g., a node’s translation, rotation, or scale (TRS).
        """

        target: Animation.Channel.Target
        """The descriptor of the animated property."""

        class Target(GLTFBase):
            """
            The descriptor of the animated property.

            Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-animation-channel-target
            """

            node: Annotated[Optional[int], Field(default=None, ge=0), IndexRef('Node')]
            """
            The index of the node to animate.
            
            When undefined, the animated object MAY be defined by an extension.
            """

            path: Literal[
                'translation',
                'rotation',
                'scale',
                'weights'
            ]
            """
            The name of the node’s TRS property to animate, or the "weights" of
            the Morph Targets it instantiates. For the "translation" property,
            the values that are provided by the sampler are the translation
            along the X, Y, and Z axes.
            
            For the "rotation" property, the values are a quaternion in the
            order (x, y, z, w), where w is the scalar.
            
            For the "scale" property, the values are the scaling factors
            along the X, Y, and Z axes.
            """

    class Sampler(GLTFBase):
        """
        An animation sampler combines timestamps with a sequence of output
        values and defines an interpolation algorithm.

        Spec: https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html#reference-animation-sampler
        """

        input: Annotated[int, Field(ge=0), IndexRef('Accessor')]
        """The index of an accessor containing keyframe timestamps."""

        interpolation: Literal['LINEAR', 'STEP', 'CUBICSPLINE'] = 'LINEAR'
        """
        Interpolation algorithm.
        
        ``"LINEAR"``
        
        The animated values are linearly interpolated between keyframes.
        When targeting a rotation, spherical linear interpolation (slerp) SHOULD be used to interpolate quaternions.
        The number of output elements MUST equal the number of input elements.
        
        ``"STEP"``
        
        The animated values remain constant to the output of the first keyframe, until the next keyframe.
        The number of output elements MUST equal the number of input elements.
        
        ``"CUBICSPLINE"``
        
        The animation’s interpolation is computed using a cubic spline with specified tangents.
        The number of output elements MUST equal three times the number of input elements.
        For each input element, the output stores three elements, an in-tangent, a spline vertex, and an out-tangent.
        There MUST be at least two keyframes when using this interpolation.
        """

        output: int = Field(ge=0)
        """The index of an accessor, containing keyframe output values."""

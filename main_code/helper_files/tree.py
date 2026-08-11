from manim import *
import numpy as np

class Tree3D(VGroup):
    def __init__(self, base_position=np.array([0, 0, -3.0]), bark_color="#5C4033", leaf_color="#2E8B57", **kwargs):
        super().__init__(**kwargs)
        
        self.bark_color = bark_color
        self.leaf_color = leaf_color
        
        self.trunk = VGroup()
        self.main_branches = VGroup()
        self.small_branches = VGroup()
        self.leaves = VGroup()

        trunk_start = base_position
        trunk_end = base_position + np.array([0, 0, 2.5])
        self.trunk.add(Line3D(start=trunk_start, end=trunk_end, thickness=0.22, color=self.bark_color))

        main_branch_ends = []
        num_main = 3
        for i in range(num_main):
            angle = i * (2 * PI / num_main)
            end_pt = trunk_end + np.array([np.cos(angle) * 0.9, np.sin(angle) * 0.9, 1.2])
            self.main_branches.add(Line3D(start=trunk_end, end=end_pt, thickness=0.12, color=self.bark_color))
            main_branch_ends.append(end_pt)

        num_twigs_per_main = 4
        for idx, main_end in enumerate(main_branch_ends):
            for j in range(num_twigs_per_main):
                angle = j * (2 * PI / num_twigs_per_main) + (idx * 0.5)
                
                twig_end = main_end + np.array([
                    np.cos(angle) * 0.7, 
                    np.sin(angle) * 0.7, 
                    0.9
                ])
                self.small_branches.add(Line3D(start=main_end, end=twig_end, thickness=0.05, color=self.bark_color))

                leaf_clusters = [
                    np.array([0.0, 0.0, 0.0]),
                    np.array([0.2, 0.1, 0.1]),
                    np.array([-0.2, -0.1, 0.1]),
                    np.array([0.1, 0.2, -0.1]),
                    np.array([-0.1, -0.2, -0.1]),
                    np.array([0.0, 0.0, 0.25])
                ]
                for offset in leaf_clusters:
                    self.leaves.add(Dot3D(point=twig_end + offset, radius=0.22, color=self.leaf_color))

        self.add(self.trunk, self.main_branches, self.small_branches, self.leaves)

class AnimateTree(AnimationGroup):
    def __init__(self, tree: Tree3D, **kwargs):
        animations = [
            Create(tree.trunk),
            AnimationGroup(*[Create(b) for b in tree.main_branches]),
            AnimationGroup(*[Create(sb) for sb in tree.small_branches]),
            AnimationGroup(*[GrowFromCenter(l) for l in tree.leaves])
        ]
        super().__init__(*animations, lag_ratio=0.55, **kwargs)

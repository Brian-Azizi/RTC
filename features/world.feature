Feature: World

  Scenario: Creating a world
    Given w ← world()
    Then w contains no objects
    And w has no light source

  Scenario: The default world
    Given light ← point_light(point(-10, 10, -10), color(1, 1, 1))
    And s1 ← sphere()
    And m ← material()
    And c ← color(0.8, 1.0, 0.6)
    And m.color ← c
    And m.diffuse ← 0.7
    And m.specular ← 0.2
    And s1.material ← m
    And s2 ← sphere()
    And transform ← scaling(0.5, 0.5, 0.5)
    And set_transform(s2, transform)
    When w ← default_world()
    Then w.light = light
    And w contains s1
    And w contains s2
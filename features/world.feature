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

  Scenario: Intersect a world with a ray
    Given w ← default_world()
    And r ← ray(point(0, 0, -5), vector(0, 0, 1))
    When xs ← intersect_world(w, r)
    Then xs.count = 4
    And xs[0].t = 4
    And xs[1].t = 4.5
    And xs[2].t = 5.5
    And xs[3].t = 6

  Scenario: Shading an intersection
    Given w ← default_world()
    And r ← ray(point(0, 0, -5), vector(0, 0, 1))
    And shape ← object 1 in w
    And i ← intersection(4, shape)
    When comps ← prepare_computations(i, r)
    And c ← shade_hit(w, comps)
    Then c = color(0.38066, 0.47583, 0.2855)

  Scenario: Shading an intersection from the inside
    Given w ← default_world()
    And l ← point_light(point(0, 0.25, 0), color(1, 1, 1))
    And w.light ← l
    And r ← ray(point(0, 0, 0), vector(0, 0, 1))
    And shape ← object 2 in w
    And i ← intersection(0.5, shape)
    When comps ← prepare_computations(i, r)
    And c ← shade_hit(w, comps)
    Then c = color(0.90498, 0.90498, 0.90498)

  Scenario: The color when a ray misses
    Given w ← default_world()
    And r ← ray(point(0, 0, -5), vector(0, 1, 0))
    When c ← color_at(w, r)
    Then c = color(0, 0, 0)

  Scenario: The color when a ray hits
    Given w ← default_world()
    And r ← ray(point(0, 0, -5), vector(0, 0, 1))
    When c ← color_at(w, r)
    Then c = color(0.38066, 0.47583, 0.2855)

  Scenario: The color with an intersection behind the ray
    Given w ← default_world()
    And outer ← object 1 in w
    And outer.material.ambient ← 1
    And inner ← object 2 in w
    And inner.material.ambient ← 1
    And r ← ray(point(0, 0, 0.75), vector(0, 0, -1))
    When c ← color_at(w, r)
    Then c = inner.material.color

  Scenario: There is no shadow when nothing is collinear with point and light
    Given w ← default_world()
    And p ← point(0, 10, 0)
    And s ← is_shadowed(w, p)
    Then s is false

  Scenario: The shadow when an object is between the point and the light
    Given w ← default_world()
    And p ← point(10, -10, 10)
    And s ← is_shadowed(w, p)
    Then s is true

  Scenario: There is no shadow when an object is behind the light
    Given w ← default_world()
    And p ← point(-20, 20, -20)
    And s ← is_shadowed(w, p)
    Then s is false

  Scenario: There is no shadow when an object is behind the point
    Given w ← default_world()
    And p ← point(-2, 2, -2)
    And s ← is_shadowed(w, p)
    Then s is false

  Scenario: shade_hit() is given an intersection in shadow
    Given w ← world()
    And p ← point_light(point(0, 0, -10), color(1, 1, 1))
    And w.light ← p
    And s1 ← sphere()
    And s1 is added to w
    And s2 ← sphere()
    And set_transform(s2, translation(0, 0, 10))
    And s2 is added to w
    And r ← ray(point(0, 0, 5), vector(0, 0, 1))
    And i ← intersection(4, s2)
    When comps ← prepare_computations(i, r)
    And c ← shade_hit(w, comps)
    Then c = color(0.1, 0.1, 0.1)
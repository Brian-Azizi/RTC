Feature: Camera

  Scenario: Constructing a camera
    Given hsize ← 160
    And vsize ← 120
    # π/2
    And field_of_view ← 1.5707963267948966
    When c ← camera(hsize, vsize, field_of_view)
    Then c.hsize = 160
    And c.vsize = 120
    And c.field_of_view = 1.5707963267948966
    And c.transform = identity_matrix

  Scenario: The pixel size for a horizontal canvas
    Given c ← camera(200, 125, 1.5707963267948966)
    Then c.pixel_size = 0.01

  Scenario: The pixel size for a vertical canvas
    Given c ← camera(125, 200, 1.5707963267948966)
    Then c.pixel_size = 0.01

  Scenario: Constructing a ray through the center of the canvas
    Given c ← camera(201, 101, 1.5707963267948966)
    When r ← ray_for_pixel(c, 100, 50)
    Then r.origin = point(0, 0, 0)
    And r.direction = vector(0, 0, -1)

  Scenario: Constructing a ray through a corner of the canvas
    Given c ← camera(201, 101, 1.5707963267948966)
    When r ← ray_for_pixel(c, 0, 0)
    Then r.origin = point(0, 0, 0)
    And r.direction = vector(0.6651864261194508, 0.3325932130597254, -0.6685123582500481)

  Scenario: Constructing a ray when the camera is transformed
    Given c ← camera(201, 101, 1.5707963267948966)
    And t1 ← rotation_y(π / 4)
    And t2 ← translation(0, -2, 5)
    And t ← t1 * t2
    When c.transform ← t
    And r ← ray_for_pixel(c, 100, 50)
    Then r.origin = point(0, 2, -5)
    # √2/2
    And r.direction = vector(0.7071067811865476, 0, -0.7071067811865476)

  Scenario: Rendering a world with a camera
    Given w ← default_world()
    And c ← camera(11, 11, 1.5707963267948966)
    And from ← point(0, 0, -5)
    And to ← point(0, 0, 0)
    And up ← vector(0, 1, 0)
    And transform ← view_transform(from, to, up)
    And c.transform ← transform
    And result ← color(0.38066119308103435, 0.47582649135129296, 0.28549589481077575)
    When image ← render(c, w)
    Then pixel_at(image, 5, 5) = result

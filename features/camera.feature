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
from pxr import Usd, UsdGeom, Gf

def compute_bbox(prim: Usd.Prim) -> Gf.Range3d:
    """
    Compute Bounding Box using ComputeWorldBound at UsdGeom.Imageable
    See https://graphics.pixar.com/usd/release/api/class_usd_geom_imageable.html

    Args:
        prim: A prim to compute the bounding box.
    Returns: 
        A range (i.e. bounding box), see more at: https://graphics.pixar.com/usd/release/api/class_gf_range3d.html
    """
    imageable = UsdGeom.Imageable(prim)
    time = Usd.TimeCode.Default() # The time at which we compute the bounding box
    bound = imageable.ComputeWorldBound(time, UsdGeom.Tokens.default_)
    bound_range = bound.ComputeAlignedBox()
    return bound_range
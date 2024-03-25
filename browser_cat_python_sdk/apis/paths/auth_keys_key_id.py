from browser_cat_python_sdk.paths.auth_keys_key_id.get import ApiForget
from browser_cat_python_sdk.paths.auth_keys_key_id.put import ApiForput
from browser_cat_python_sdk.paths.auth_keys_key_id.delete import ApiFordelete
from browser_cat_python_sdk.paths.auth_keys_key_id.patch import ApiForpatch


class AuthKeysKeyId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass

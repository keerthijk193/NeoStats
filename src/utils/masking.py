import hashlib


def mask_email(email):
    return hashlib.sha256(str(email).encode()).hexdigest()


def mask_phone(phone):
    phone = str(phone)
    return "XXXXXX" + phone[-4:]


def apply_masking(df):
    df["email"] = df["email"].apply(mask_email)
    df["phone"] = df["phone"].apply(mask_phone)

    return df

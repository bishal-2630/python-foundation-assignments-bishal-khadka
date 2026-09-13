

# Transformation logic under test
HIGH_VALUE_THRESHOLD = 10000


def is_high_value(amount, threshold=HIGH_VALUE_THRESHOLD):
    return float(amount) >= threshold


def categorize(total, has_defaulted_loan=False):
    if has_defaulted_loan:
        return "At Risk"
    if total >= 20000:
        return "Premium"
    elif total >= 5000:
        return "Standard"
    else:
        return "Basic"


def transform_loans(rows):
    per_customer = {}
    for row in rows:
        cid = row["customer_id"]
        entry = per_customer.setdefault(
            cid,
            {"total_loan_exposure": 0.0, "active_loan_count": 0, "has_defaulted": False},
        )
        if row["status"] == "active":
            entry["total_loan_exposure"] += float(row["principal"])
            entry["active_loan_count"] += 1
        if row["status"] == "defaulted":
            entry["has_defaulted"] = True

    return per_customer



# categorize() tests

def test_categorize_premium_boundary():
    assert categorize(20000) == "Premium"


def test_categorize_just_below_premium():
    assert categorize(19999.99) == "Standard"


def test_categorize_standard_boundary():
    assert categorize(5000) == "Standard"


def test_categorize_below_standard_is_basic():
    assert categorize(4999.99) == "Basic"


def test_categorize_defaulted_overrides_high_total():
    assert categorize(50000, has_defaulted_loan=True) == "At Risk"


def test_categorize_defaulted_overrides_low_total():
    assert categorize(0, has_defaulted_loan=True) == "At Risk"


def test_categorize_no_default_flag_behaves_normally():
    assert categorize(9050) == "Standard"



# transform_loans() tests

def test_transform_loans_zero_loans():
    result = transform_loans([])
    assert result == {}


def test_transform_loans_only_active_counts_toward_exposure():
    rows = [
        {"customer_id": 1, "principal": 5000.00, "status": "active"},
        {"customer_id": 1, "principal": 2000.00, "status": "paid_off"},
    ]
    result = transform_loans(rows)
    assert result[1]["total_loan_exposure"] == 5000.00
    assert result[1]["active_loan_count"] == 1
    assert result[1]["has_defaulted"] is False


def test_transform_loans_defaulted_flag_set_correctly():
    rows = [
        {"customer_id": 2, "principal": 15000.00, "status": "active"},
        {"customer_id": 2, "principal": 8000.00, "status": "defaulted"},
    ]
    result = transform_loans(rows)
    assert result[2]["has_defaulted"] is True
    assert result[2]["total_loan_exposure"] == 15000.00
    assert result[2]["active_loan_count"] == 1


def test_transform_loans_multiple_customers_are_independent():
    rows = [
        {"customer_id": 1, "principal": 5000.00, "status": "active"},
        {"customer_id": 2, "principal": 15000.00, "status": "active"},
        {"customer_id": 2, "principal": 8000.00, "status": "defaulted"},
        {"customer_id": 3, "principal": 3000.00, "status": "active"},
        {"customer_id": 3, "principal": 1000.00, "status": "paid_off"},
    ]
    result = transform_loans(rows)
    assert set(result.keys()) == {1, 2, 3}
    assert result[1]["has_defaulted"] is False
    assert result[2]["has_defaulted"] is True
    assert result[3]["total_loan_exposure"] == 3000.00
    assert result[3]["active_loan_count"] == 1


def test_transform_loans_customer_with_only_paid_off_has_zero_exposure():
    rows = [
        {"customer_id": 4, "principal": 2000.00, "status": "paid_off"},
    ]
    result = transform_loans(rows)
    assert result[4]["total_loan_exposure"] == 0.0
    assert result[4]["active_loan_count"] == 0
    assert result[4]["has_defaulted"] is False

# is_high_value() tests

def test_high_value_flag_true_at_threshold():
    assert is_high_value(10000) is True


def test_high_value_flag_false_below_threshold():
    assert is_high_value(9999.99) is False


def test_high_value_flag_true_above_threshold():
    assert is_high_value(30000) is True


def test_high_value_flag_custom_threshold():
    assert is_high_value(4000, threshold=3000) is True
    assert is_high_value(2000, threshold=3000) is False
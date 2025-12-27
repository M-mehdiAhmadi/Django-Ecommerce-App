
# Django E-Commerce App (Reusable Package)

A **complete, reusable Django e-commerce application** with dynamic models, flexible admin interface, and full test coverage.  
Perfect for integrating into any Django project as a pluggable e-commerce module.

Official Django guide for reusable apps:  
https://docs.djangoproject.com/en/stable/intro/reusable-apps/

---

## Features

✅ **Complete E-Commerce Models**
- `Product` + `ProductVariant` (SKU-based, multi-variant support)
- `Category` (hierarchical/tree structure)
- `ProductAttribute` & `ProductAttributeValue` (dynamic attributes: Color, Size, etc.)
- `ProductImage` (multiple images per product/variant)
- `Inventory` (stock management with reservation support)
- `Customer` & `Address` (customer profiles and addresses)
- `Order` & `OrderItem` (order management with price snapshots)
- `PaymentTransaction` (payment audit trail)
- `Coupon` (discount management)

✅ **Django Admin Integration**
- Full admin interface for all models
- Inline editors for variants and images
- Custom filters and search
- Bulk actions and customized displays

✅ **Dynamic & Reusable Design**
- `JSONField` support for extensible data (metadata)
- No hardcoded business logic—easy to customize
- Proper indexing and constraints for production
- i18n-ready (gettext translations)

✅ **Testing**
- Comprehensive pytest-based unit tests
- No database required (uses in-memory SQLite)
- Integration tests for complex workflows

---

## Project Structure

```
Django-Ecommerce-App/
│
├── Django_Ecommerce_App/              # Main app package
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py                      # All e-commerce models
│   ├── admin.py                       # Admin configuration
│   ├── views.py                       # Views (to be implemented)
│   ├── urls.py                        # URL routing
│   ├── forms.py                       # Forms (to be implemented)
│   ├── test.py                        # Django tests
│   │
│   ├── migrations/                    # Auto-generated migrations
│   ├── templates/Django_Ecommerce_App/
│   └── static/Django_Ecommerce_App/
│
├── tests/                             # pytest tests
│   ├── conftest.py                    # pytest configuration
│   ├── settings.py                    # Django test settings
│   └── test_models.py                 # Model tests
│
├── pytest.ini                         # pytest configuration
├── requirements-dev.txt               # Development dependencies
├── pyproject.toml
├── setup.py
├── LICENSE
├── README.md
└── MANIFEST.in
```

---

## Installation

### 1. Install Dependencies

```bash
pip install Django>=5.0
pip install -e .  # Install this package in development mode
```

### 2. Add to Django Project

In your Django project's `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # ...
    'Django_Ecommerce_App',  # Add this
]
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

---

## Usage

### Basic Example: Creating Products

```python
from Django_Ecommerce_App.models import Category, Product, ProductVariant, Inventory

# Create a category
electronics = Category.objects.create(
    name="Electronics",
    slug="electronics",
    description="Electronic devices"
)

# Create a product
laptop = Product.objects.create(
    name="MacBook Pro",
    slug="macbook-pro",
    description="High-performance laptop",
    status="published",
    is_active=True
)
laptop.categories.add(electronics)

# Create variants (SKU-based)
variant1 = ProductVariant.objects.create(
    product=laptop,
    sku="MBPRO-16-M1-256",
    name="16-inch M1 256GB",
    price=Decimal('1999.99'),
    compare_price=Decimal('2499.99'),
    is_default=True
)

# Manage inventory
inventory = Inventory.objects.create(
    variant=variant1,
    quantity=50,
    reorder_level=10
)

# Check available stock
print(f"Available: {inventory.available_quantity}")
```

### Admin Interface

Navigate to `/admin/` to manage all e-commerce data:
- Add/edit products, variants, and attributes
- Manage inventory and stock levels
- Track orders and payments
- Create and manage discount coupons

---

## Testing

### Run All Tests (Pytest)

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run with coverage
pytest --cov=Django_Ecommerce_App tests/
```

### Test Coverage

- Model creation and validation
- Inventory management (reserve, release, reduce)
- Price calculations (discounts, totals)
- Order processing
- Coupon validation and discount calculation

---

## API / Utility Methods

### Product
- `get_default_variant()` - Get default variant
- `get_min_price()` - Lowest price among variants
- `get_max_price()` - Highest price among variants

### ProductVariant
- `get_discount_percentage()` - Calculate discount if `compare_price` is set

### Inventory
- `reserve(qty)` - Reserve stock for an order
- `release(qty)` - Release reserved stock
- `reduce_stock(qty)` - Deduct from inventory (on fulfillment)
- `available_quantity` - Property: quantity - reserved
- `is_low_stock` - Property: check if below reorder level

### Order
- `calculate_total()` - Recalculate total from items and fees

### OrderItem
- `get_total()` - Calculate item total (quantity × unit_price)

### Coupon
- `is_valid()` - Check if coupon is currently valid
- `calculate_discount(amount)` - Compute discount for given amount

---

## Models Overview

### Category
- Hierarchical/nested categories
- SEO-friendly slugs
- Status control (is_active)
- Metadata support (JSON)

### Product
- Name, description, short_description
- Status: draft, published, archived
- Categories (M2M)
- SEO fields (meta_title, meta_description)
- Metadata (JSON) for custom fields

### ProductVariant
- SKU (unique identifier)
- Price and compare_price (for discounts)
- Weight (for shipping)
- Dynamic attributes (Color, Size, etc. as JSON)
- is_default flag (primary variant)
- Metadata for variant-specific data

### ProductAttribute & ProductAttributeValue
- Dynamic attribute system for filters and variants
- Input types: select, text, number, color, checkbox
- Filterable and visible flags

### ProductImage
- Multiple images per product or variant
- Alt text for SEO
- Position for ordering
- Primary image flag

### Inventory
- One-to-one with ProductVariant
- Quantity and reserved tracking
- Reorder level for low-stock alerts
- Helper methods for stock operations

### Customer
- User profile (linked to Django User)
- Contact info (email, phone)
- Default shipping and billing addresses

### Address
- Shipping and billing addresses
- Full postal information
- Linked to Customer (optional)

### Order
- Order number (unique)
- Customer and addresses
- Status: pending, processing, shipped, delivered, cancelled
- Payment status: pending, paid, failed, refunded
- Price breakdown: subtotal, tax, shipping, discount, total
- Currency support
- Order notes and metadata

### OrderItem
- Snapshot of product data at order time
- Links to variant (can be null if variant deleted)
- Quantity and unit price
- Total calculation

### PaymentTransaction
- Multiple providers: Stripe, PayPal, Bank Transfer, Cash
- Unique transaction ID
- Status tracking: pending, completed, failed, refunded
- JSON payload for provider-specific data

### Coupon
- Code and description
- Discount types: percentage or fixed amount
- Max discount limit
- Usage limits (total and per customer)
- Validity dates
- Minimum purchase amount
- Category restrictions

---

## Customization

### Adding Custom Fields

Since models use `JSONField` for metadata, you can:

1. **Add temporary custom data** without migration:
```python
product.metadata = {
    'warranty_months': 24,
    'brand_id': 42,
}
product.save()
```

2. **Extend models** with custom inheritance:
```python
from Django_Ecommerce_App.models import Product

class MyProduct(Product):
    warranty_months = models.IntegerField(default=12)
```

### Custom Admin Actions

Extend `admin.py` to add bulk actions, exports, etc.

---

## API Views (To Be Implemented)

Recommended endpoints:
- `GET /api/products/` - List products
- `GET /api/products/<slug>/` - Product detail
- `GET /api/categories/` - List categories
- `POST /api/cart/add/` - Add to cart
- `POST /api/orders/create/` - Create order
- `POST /api/coupons/validate/` - Validate coupon

---

## Contributing

See `CONTRIBUTING.md` (to be created) for guidelines on:
- Adding new models or fields
- Extending admin interface
- Writing tests
- Submitting pull requests

---

## License

See `LICENSE` file.

---

## Support & Documentation

For Django app development best practices:
- https://docs.djangoproject.com/en/stable/intro/reusable-apps/
- https://docs.djangoproject.com/en/stable/topics/db/models/
- https://docs.djangoproject.com/en/stable/ref/contrib/admin/


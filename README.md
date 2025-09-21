# Odoo 18 Development & Production Environment

🚀 **Status:** FULLY OPERATIONAL! Odoo 18 accessible at http://174.138.93.20:8069

⚠️ **Note**: SSH access temporarily blocked by UFW firewall. Use DigitalOcean console for server access.

## 🚀 Quick Start

### Development Environment

1. **Start development environment:**
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

2. **Access Odoo:**
   - URL: http://localhost:8069
   - Master Password: `w6kh-tdxq-ar2z`

3. **Stop development environment:**
   ```bash
   docker-compose -f docker-compose.dev.yml down
   ```

### Production Deployment

Production deployment is automated via GitHub Actions when you push to the `main` branch.

## 📁 Directory Structure

```
/
├── odoo-source/           # Editable Odoo source code
├── custom-addons/         # Your custom modules
├── config/               # Configuration files
├── data/                 # Local data persistence (gitignored)
├── logs/                 # Log files (gitignored)
├── docker-compose.dev.yml # Development environment
├── docker-compose.prod.yml # Production environment
└── .github/workflows/     # Deployment automation
```

## 🔧 Development Workflow

1. **Edit source code** in `odoo-source/` directory
2. **Create custom modules** in `custom-addons/`
3. **Test locally** with development environment
4. **Commit changes** and push to trigger deployment

## 📚 More Information

See `CLAUDE.md` for comprehensive documentation and setup details.# Fresh deployment trigger

# Odoo 18 Development & Production Environment

## 📋 Project Overview

**Complete Odoo 18 development and production setup with editable source code, custom addon development, and automated deployment to DigitalOcean.**

### 🎯 Current Status: **FULLY OPERATIONAL** ✅

- **Odoo Version**: 18 (Latest Stable Community Edition)
- **Database**: PostgreSQL 15
- **Development Access**: http://localhost:8069
- **Production Server**: http://167.71.113.65:8069
- **Production Database**: `production`
- **Admin Login**: vicky@clyvanta.com
- **Master Password**: `w6kh-tdxq-ar2z`
- **Location**: `/Users/vicky/Desktop/Vicky/Ventures/Odoo/Odoo`
- **GitHub Repository**: https://github.com/vicky3074/Odoo18-Production
- **Deployment**: Automated via GitHub Actions

---

## 🏗️ Architecture & File Structure

### Development Environment Structure
```
/Users/vicky/Desktop/Vicky/Ventures/Odoo/Odoo/
├── odoo-source/               # Editable Odoo 18 source code (41K+ files)
├── custom-addons/             # Your custom modules
│   └── sample_addon/         # Example custom addon
├── config/
│   ├── odoo.conf             # Production configuration
│   └── odoo.dev.conf         # Development configuration
├── data/                     # Local data persistence (gitignored)
├── logs/                     # Development logs (gitignored)
├── docker-compose.dev.yml    # Development environment
├── docker-compose.prod.yml   # Production environment
├── Dockerfile.prod           # Production Docker image
├── .github/workflows/        # Deployment automation
│   └── deploy.yml           # GitHub Actions pipeline
├── .gitignore               # Git exclusions
└── CLAUDE.md                # This documentation
```

### Dual Environment Architecture

**Development Environment:**
- **Purpose**: Local development with hot-reload capabilities
- **Odoo Source**: Available for editing in `odoo-source/`
- **Custom Addons**: Mounted from `custom-addons/`
- **Database**: PostgreSQL 15 (exposed on port 5432 for development)
- **Access**: http://localhost:8069

**Production Environment:**
- **Purpose**: Automated deployment to DigitalOcean
- **Docker Image**: Custom built from Dockerfile.prod
- **Deployment**: GitHub Actions → DigitalOcean (167.71.113.65)
- **SSL**: Ready for setup
- **Domain**: Ready for configuration

### Data Storage Locations
- **Development Data**: Docker volumes (odoo-dev-*)
- **Production Data**: DigitalOcean server volumes
- **Source Code**: Local filesystem (`odoo-source/`)
- **Custom Modules**: Local filesystem (`custom-addons/`)

---

## 🚀 Development Workflow

### Daily Development Commands

```bash
# Navigate to project directory
cd "/Users/vicky/Desktop/Vicky/Ventures/Odoo/Odoo"

# Start development environment
docker-compose -f docker-compose.dev.yml up -d

# Access Odoo: http://localhost:8069
# Master Password: w6kh-tdxq-ar2z

# View development logs
docker-compose -f docker-compose.dev.yml logs -f odoo

# Stop development environment
docker-compose -f docker-compose.dev.yml down

# Restart after changes
docker-compose -f docker-compose.dev.yml restart odoo
```

### Source Code Development

```bash
# Edit Odoo core (if needed)
# Files: odoo-source/addons/*/
# Note: Core changes should be minimal

# Create custom modules
mkdir -p custom-addons/my_module
# Edit: custom-addons/my_module/__manifest__.py

# Hot reload addon changes
# Odoo automatically detects custom addon changes
```

### Production Deployment

```bash
# Setup GitHub repository (one-time)
# 1. Create GitHub repo: "Odoo18-Production"
# 2. Add secrets: SSH_PRIVATE_KEY, SERVER_HOST, DB_PASSWORD
# 3. Push code to main branch

# Deploy to production (automatic)
git add .
git commit -m "feat: your changes"
git push origin main  # Triggers GitHub Actions deployment

# Manual deployment test
gh workflow run deploy.yml  # If GitHub CLI installed
```

### System Information Commands

```bash
# Check Docker disk usage
docker system df

# Check container resource usage
docker stats

# List Docker volumes
docker volume ls | grep odoo

# Inspect Odoo data volume
docker volume inspect odoo_odoo-web-data

# Access Odoo container shell
docker exec -it odoo-odoo-1 /bin/bash

# Check Odoo source code location
docker exec odoo-odoo-1 ls -la /usr/lib/python3/dist-packages/odoo/
```

---

## 🔧 Configuration Details

### Docker Compose Configuration
```yaml
services:
  db:
    image: postgres:15
    user: root
    environment:
      - POSTGRES_PASSWORD=myodoo
      - POSTGRES_USER=odoo
      - POSTGRES_DB=postgres
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - odoo-db-data:/var/lib/postgresql/data/pgdata
    restart: unless-stopped

  odoo:
    image: odoo:18
    user: root
    depends_on:
      - db
    ports:
      - "8069:8069"
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=myodoo
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./config:/etc/odoo
      - ./addons:/mnt/extra-addons
    restart: unless-stopped

volumes:
  odoo-web-data:
  odoo-db-data:
```

### Odoo Configuration (`config/odoo.conf`)
```ini
[options]
admin_passwd = $pbkdf2-sha512$600000$Zay1traWkvI.51zr3btXSg$tZ3VPN0zkqYe7uft.PBhFylsp2HxdUfBMS8rURtKF3MLx4zKHH1fQPydTh3y05rnudruSWN8w/jyfV3kI93pkw
db_host = db
db_port = 5432
db_user = odoo
db_password = myodoo
addons_path = /mnt/extra-addons
data_dir = /var/lib/odoo
logfile = /var/log/odoo/odoo.log
log_level = info
```

---

## 📊 Database Information

### Production Database
- **Name**: `production`
- **Admin User**: vicky@clyvanta.com
- **Admin Password**: [Set during database creation]
- **Phone**: 6479365467
- **Country**: Canada
- **Language**: English (US)
- **Demo Data**: Enabled (includes sample data for testing)
- **Status**: ✅ Active and operational

### Database Management
- **Master Password**: `w6kh-tdxq-ar2z` (for database operations)
- **Database Operations**: Create, backup, restore, duplicate databases
- **Production Access**: http://167.71.113.65:8069/web/database/manager
- **Development Access**: http://localhost:8069/web/database/manager

### Access URLs
- **Production Odoo**: http://167.71.113.65:8069
- **Development Odoo**: http://localhost:8069
- **Database Manager**: http://167.71.113.65:8069/web/database/manager

---

## 🔌 Available Apps & Modules

### Installed Core Apps (55 official apps available)
The system includes standard Odoo Community apps:

**Key Business Apps:**
- Sales, CRM, Invoicing
- Inventory, Purchase, Manufacturing
- Accounting, Project Management
- Website, eCommerce
- HR, Timesheets, Expenses
- Marketing, Email Marketing

**Note**: Some apps may show "Upgrade" instead of "Install" - this is normal behavior for dependency resolution and ensures latest versions.

### Custom Apps Directory
- **Location**: `./addons/` (currently empty)
- **Usage**: Place custom/third-party modules here
- **Access**: Automatically scanned by Odoo

---

## 🌐 Access & Networking

### Production Access
- **Primary URL**: http://167.71.113.65:8069
- **Database Manager**: http://167.71.113.65:8069/web/database/manager
- **Port**: 8069 (externally accessible)
- **Firewall**: UFW configured for SSH (22) and HTTP (8069)

### Development Access
- **Primary URL**: http://localhost:8069
- **Network Access**: http://[YOUR_LOCAL_IP]:8069
- **Port Mapping**: `0.0.0.0:8069->8069/tcp` (all interfaces)

### Security Considerations
- **Database Port**: 5432 (internal Docker network only)
- **Master Password**: Encrypted and stored securely
- **User Authentication**: Standard Odoo session management
- **Firewall**: UFW enabled with SSH and HTTP access

---

## 📈 Performance & Resource Usage

### Current Resource Usage
- **Odoo Image Size**: 3.04GB
- **Total Docker Usage**: ~19.77GB (includes all images)
- **Active Volumes**: 3.042GB
- **Container Overhead**: 528.4kB

### Performance Monitoring
```bash
# Monitor container performance
docker stats odoo-odoo-1 odoo-db-1

# Check container logs for errors
docker-compose logs --tail=100 odoo
docker-compose logs --tail=100 db
```

---

## 🔄 Backup & Maintenance

### Database Backup
```bash
# Backup specific database
docker-compose exec db pg_dump -U odoo Clyvanta > clyvanta_backup_$(date +%Y%m%d).sql

# Backup all databases
docker-compose exec db pg_dumpall -U odoo > full_backup_$(date +%Y%m%d).sql
```

### Volume Backup
```bash
# Backup Odoo data volume
docker run --rm -v odoo_odoo-web-data:/data -v $(pwd):/backup alpine tar czf /backup/odoo-data-backup.tar.gz -C /data .

# Backup database volume
docker run --rm -v odoo_odoo-db-data:/data -v $(pwd):/backup alpine tar czf /backup/db-data-backup.tar.gz -C /data .
```

### Maintenance Tasks
```bash
# Clean up unused Docker resources
docker system prune -a

# Update containers to latest versions
docker-compose pull
docker-compose up -d

# Recreate containers (preserves data)
docker-compose down
docker-compose up -d
```

---

## 🚀 Scaling & Cloud Deployment

### Resource Requirements for Cloud Hosting

**Small Business (1-5 users):**
- CPU: 2 cores
- RAM: 4GB
- Storage: 40GB SSD
- Cost: ~$20-40/month

**Growing Business (5-25 users):**
- CPU: 4 cores
- RAM: 8GB
- Storage: 80GB SSD
- Cost: ~$40-80/month

**Enterprise (25+ users):**
- CPU: 8+ cores
- RAM: 16GB+
- Storage: 200GB+ SSD
- Load balancing recommended
- Cost: ~$150-500+/month

### Cloud Deployment Options
- **DigitalOcean**: Budget-friendly droplets
- **AWS EC2**: Enterprise-grade with auto-scaling
- **Google Cloud**: Competitive pricing
- **Linode/Vultr**: Simple and cost-effective

---

## 🛠️ Troubleshooting Guide

### Common Issues & Solutions

#### Containers Won't Start
```bash
# Check container status
docker-compose ps

# Check logs for errors
docker-compose logs

# Restart services
docker-compose down && docker-compose up -d
```

#### Port Already in Use
```bash
# Find process using port 8069
lsof -i :8069

# Kill process or change port in docker-compose.yml
# ports: - "8070:8069"  # Use port 8070 instead
```

#### Database Connection Issues
```bash
# Check database container
docker-compose logs db

# Restart database
docker-compose restart db

# Verify database is accepting connections
docker-compose exec db psql -U odoo -d postgres -c "SELECT 1;"
```

#### Performance Issues
```bash
# Check resource usage
docker stats

# Increase container resources (if needed)
# Add to docker-compose.yml:
# deploy:
#   resources:
#     limits:
#       memory: 2G
```

#### "Upgrade" vs "Install" Apps
- **Normal behavior** on fresh installations
- **Click "Upgrade"** to install latest version
- **Safe operation** - no data loss risk

---

## 📝 Development & Customization

### Custom Module Development
```bash
# Create custom module directory
mkdir -p ./addons/my_custom_module

# Module structure
./addons/my_custom_module/
├── __init__.py
├── __manifest__.py
└── models/
    └── __init__.py
```

### Development Mode
```bash
# Enable developer mode in Odoo:
# Settings → Activate Developer Mode
# Or add ?debug=1 to URL
```

### Log Level Configuration
Edit `config/odoo.conf`:
```ini
log_level = debug  # For detailed debugging
log_level = info   # Standard logging
log_level = warn   # Minimal logging
```

---

## 🔗 Useful Resources

### Documentation
- **Odoo Documentation**: https://www.odoo.com/documentation/18.0/
- **Odoo Apps Store**: https://apps.odoo.com
- **Community Forum**: https://www.odoo.com/forum
- **Docker Hub**: https://hub.docker.com/_/odoo

### Development Resources
- **Odoo GitHub**: https://github.com/odoo/odoo
- **Development Guide**: https://www.odoo.com/documentation/18.0/developer.html
- **API Reference**: https://www.odoo.com/documentation/18.0/reference.html

---

## 📞 Quick Reference

### Key Information
- **Project Location**: `/Users/vicky/Desktop/Vicky/Ventures/Odoo/Odoo`
- **Access URL**: http://localhost:8069
- **Database**: Clyvanta
- **Admin**: vicky@clyvanta.com
- **Master Password**: w6kh-tdxq-ar2z

### Essential Commands
```bash
# Start: docker-compose up -d
# Stop: docker-compose down
# Logs: docker-compose logs -f odoo
# Status: docker-compose ps
```

---

*Last Updated: September 2025*
*Odoo Version: 18 Community Edition*
*Setup Type: Local Docker Development Environment*
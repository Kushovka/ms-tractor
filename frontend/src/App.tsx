import { Navigate, Route, Routes } from 'react-router'
import { Layout } from './components/Layout'
import { AboutPage } from './pages/AboutPage'
import { ContactPage } from './pages/ContactPage'
import { DeliveryPage } from './pages/DeliveryPage'
import { GuaranteePage } from './pages/GuaranteePage'
import { HomePage } from './pages/HomePage'
import { InventoryPage } from './pages/InventoryPage'
import { MaintenancePage } from './pages/MaintenancePage'
import { PrivacyPage } from './pages/PrivacyPage'
import { TermsPage } from './pages/TermsPage'
import { TeamPage } from './pages/TeamPage'
import { VehicleDetailPage } from './pages/VehicleDetailPage'
import { WarrantyPage } from './pages/WarrantyPage'

const maintenanceMode = import.meta.env.VITE_MAINTENANCE_MODE === 'true'

const App = () => (
  <Routes>
    {maintenanceMode ? (
      <Route path="*" element={<MaintenancePage />} />
    ) : (
      <Route element={<Layout />}>
        <Route index element={<HomePage />} />
        <Route path="inventory" element={<InventoryPage />} />
        <Route path="inventory/:slug" element={<VehicleDetailPage />} />
        <Route path="delivery" element={<DeliveryPage />} />
        <Route path="guarantee" element={<GuaranteePage />} />
        <Route path="warranty" element={<WarrantyPage />} />
        <Route path="about" element={<AboutPage />} />
        <Route path="team" element={<TeamPage />} />
        <Route path="contact" element={<ContactPage />} />
        <Route path="privacy-policy" element={<PrivacyPage />} />
        <Route path="terms" element={<TermsPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Route>
    )}
  </Routes>
)

export default App

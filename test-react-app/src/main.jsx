import {StrictMode} from 'react'
import {createRoot} from 'react-dom/client'
import './index.css'
import Header from './Header.jsx'
import CustomerDisplay from './CustomerDisplay.jsx'
import CustomerTable from './CustomerTable.jsx'

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <Header/>
        <CustomerTable/>
        {/*<CustomerDisplay/>*/}
    </StrictMode>,
)

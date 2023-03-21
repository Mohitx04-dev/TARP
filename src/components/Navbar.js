import React, { useEffect } from 'react';
import { useLocation, useHistory } from 'react-router-dom';
import { Link } from 'react-router-dom';


const Navbar = () => {

    let history = useHistory();
    const handleLogout = () => {
        localStorage.removeItem('token');
        history.push('/login');
    }
    let location = useLocation();
    useEffect(() => {
        console.log(location.pathname);
    }, [location]); //location is using to highlight navbar active component

    return <div>
        <nav className="navbar nav-adj navbar-expand-lg navbar-dark">
            <div className="container-fluid">
                <div id="logo">
                    <i className="far fa-snowflake"></i> Image <i
                        className="far fa-snowflake"></i>
                </div>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <Link className={`custom-link-class wset nav-link ${location.pathname}==="/"? "active" : ""`} aria-current="page" to="/">Home</Link>
                        </li>
                        <li className="nav-item">
                            <Link className={`custom-link-class wset nav-link ${location.pathname}==="/"? "active" : ""`} aria-current="page" to="/upload">Upload</Link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>;
};

export default Navbar;

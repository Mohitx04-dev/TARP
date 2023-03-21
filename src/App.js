import './App.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import NoteState from './context/data/NoteState';
import Navbar from './components/Navbar';
import Home from './components/Uploader';
import Downloader from './components/Downloader';
import Uploader from './components/Uploader';


function App() {
  return (
    <>
      <NoteState>
        <Router>
          <Navbar />
          <div className="container">
            <Switch>
              <Route exact path="/">
                <Downloader/>
              </Route>
              <Route exact path="/upload">
                <Uploader/>
              </Route>
            </Switch>
          </div>
        </Router>
      </NoteState>
    </>
  );
}

export default App;

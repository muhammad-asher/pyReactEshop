import Footer from "./components/Footer";
import Header from "./components/Header";
import {Container} from 'react-bootstrap'
import HomeScreen from "./screens/HomeScreen";
import {BrowserRouter ,Route,Routes} from 'react-router-dom'
import ProductScreen from "./screens/ProductScreen";
import CartScreen from "./screens/CartScreen";
function App() {
  return (
    <BrowserRouter >
      <Header />
      <main className="py-3">
      <Container>
        <Routes>
      <Route path ="/" Component={HomeScreen} exact/>
      <Route path='/product/:id' Component={ProductScreen}/>
      <Route path='/cart/:id?' Component={CartScreen} />
      </Routes>
        </Container>
      </main>
      <Footer />
    </BrowserRouter>
  );
}

export default App;

import React from 'react'
import { useEffect } from 'react' 
import { useDispatch, useSelector } from 'react-redux'
import { Link, useParams } from 'react-router-dom'
import { Row,Col, ListGroup, Image,Form ,Button } from 'react-bootstrap'
import { addToCart } from '../actions/cartActions'


const CartScreen = () => {

    const {id} = useParams();
    const searchParams = new URLSearchParams(window.location.search);

    const qty  = searchParams.get('qty');

    const dispatch = useDispatch()

    const cart = useSelector(state => state.cart)

    const {cartItems} =  cart

    console.log('cartItems',cartItems)

    useEffect(()=>{
        if(id) {
            dispatch(addToCart(id,qty))
        }
    },[dispatch, id, qty])


  return ( 
    <div>Cart</div>
  )
}

export default CartScreen
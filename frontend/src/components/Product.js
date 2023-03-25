import React from 'react'
import {Card} from 'react-bootstrap'
import Rating from './Rating'
import {Link} from 'react-router-dom'
function Product({product}) {
  return (
    <Card className='my-3 p-3 rounded'>
        <Link to={`/product/${product._id}`}>
            <Card.Img src={product.image}/>
        </Link>
        <Card.Body>
              <a href={`/product/${product._id}`}>
                  <h5>
                    <strong>
                        {product.name}
                    </strong>
                  </h5>
              </a>
        <h5 >
        <div className='my-3'>
                      <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#f8e825'}/>
        </div>
        </h5>

        
             <h3>
                ${product.price}
             </h3>
        
        </Card.Body>
    </Card>
  )
}

export default Product
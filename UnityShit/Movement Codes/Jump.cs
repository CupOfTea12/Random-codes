using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class jumpScript : MonoBehaviour
{
    public float jumpForce = 5.0f;
    private bool isJumping;
    private bool isGrounded;
    private Animator animator;


void Start(){
         animator = GetComponent<Animator>();

}
    void Update()
    {
   
        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            Jump();
            animator.SetBool("isJumping",true);
            isJumping=true;
        }
    }
 void Jump()
    {
        GetComponent<Rigidbody>().velocity = new Vector3(0, jumpForce, 0);
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Ground"))
        {
            animator.SetBool("isGrounded",true);
            isGrounded = true;
            animator.SetBool("isJumping",false);
            isJumping=false;
            animator.SetBool("isFalling",false);


        }
    }

    void OnCollisionExit(Collision collision)
    {
        if (collision.gameObject.CompareTag("Ground"))
        {
            animator.SetBool("isGrounded",false);
            isGrounded = false;

          

        }
    }
}

